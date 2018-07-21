//searchGOindangdang.go
package main

import (
	"math/rand"
	"time"
	"net/http"
	"fmt"
	"log"
	"github.com/PuerkitoBio/goquery"
	"strconv"
	"github.com/Tang-RoseChild/mahonia"
	"os"
	"encoding/csv"
)
//record [5]string   {href,url,content}  元素链接href是唯一的
//store:=make(map[string][n]string)  //爬取数据集合 key=href
//filename //保存文件
//urls:=getUrls()  //页面url集合 int==1标记已经读取
//request=geneRequest(url)
//fetchAll()
//fetchOne()

func main(){
	t1 := time.Now()
	fmt.Println("开始爬取")
	urls:=geneUrls()
	store:=make(map[string][]string)
	fetchALl(urls,store)
	fmt.Println("结束爬取")
	fmt.Println(store["http://product.dangdang.com/1900682740.html"][2])
	filename:="goondd.tsv"
	writeTSV(filename,store)
	fmt.Println(time.Since(t1))
}

func geneUrls() map[string]int{
	urls:=make(map[string]int)
	url0:="http://search.dangdang.com/?key=go&act=input&page_index="
	for i:=0; i<100; i++{
		url := url0 + strconv.Itoa(i)
		urls[url]=0
		//fmt.Println(url)
	}
	return urls
}

func fetchALl(urls map[string]int,store map[string][]string){
	for url,count:=range urls{
		if count==0{
			channel :=make(chan [][]string)
			defer close(channel)
			go fetchOne(url,channel)
			records:=<-channel
			for _,record:=range records{
				//fmt.Printf("content"+record[2])
				href:=record[0]
				if _,ok:=store[href];!ok{
					store[href]=record
				}
			}
		}
	}
}

func fetchOne(url string, channel chan <-[][]string)  {

	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("User-Agent", geneAgent())
	req.Header.Add("Referer", url)
	client := http.DefaultClient
	res, err := client.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != 200 {
		log.Fatalf("status code error: %d %s", res.StatusCode, res.Status)
	}
	//	utfBody, err := iconv.NewReader(res.Body, "GBK", "utf-8")
	dec := mahonia.NewDecoder("GBK")
	utfBody := dec.NewReader(res.Body)
	if err != nil {
		fmt.Println(err.Error())
	}
	// Load the HTML document
	doc, err := goquery.NewDocumentFromReader(utfBody)
	if err != nil {
		log.Fatal(err)
	}
	var records [][]string

	doc.Find("#search_nature_rg ul li").Each(func(i int, s *goquery.Selection) {
		href, _ := s.Find(".name a").Attr("href")
		title, _ := s.Find(".name a").Attr("title")
		link, _ := s.Find(".name a").Attr("href")
		price := s.Find(".search_now_price").Text()
		search_comment_num := s.Find(".search_comment_num").Text()
		author, _ := s.Find(".search_book_author span a").Attr("title")
		record:=[]string{href,url,title,link,price,search_comment_num,author} //个
		records= append(records, record)
		//fmt.Println(record[0])
	})
	channel<- records
}

var userAgent = [...]string{"Mozilla/5.0 (compatible, MSIE 10.0, Windows NT, DigExt)",
	"Mozilla/4.0 (compatible, MSIE 7.0, Windows NT 5.1, 360SE)",
	"Mozilla/4.0 (compatible, MSIE 8.0, Windows NT 6.0, Trident/4.0)",
	"Mozilla/5.0 (compatible, MSIE 9.0, Windows NT 6.1, Trident/5.0,",
	"Opera/9.80 (Windows NT 6.1, U, en) Presto/2.8.131 Version/11.11",
	"Mozilla/4.0 (compatible, MSIE 7.0, Windows NT 5.1, TencentTraveler 4.0)",
	"Mozilla/5.0 (Windows, U, Windows NT 6.1, en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
	"Mozilla/5.0 (Macintosh, Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh, U, Intel Mac OS X 10_6_8, en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
	"Mozilla/5.0 (Linux, U, Android 3.0, en-us, Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
	"Mozilla/5.0 (iPad, U, CPU OS 4_3_3 like Mac OS X, en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
	"Mozilla/4.0 (compatible, MSIE 7.0, Windows NT 5.1, Trident/4.0, SE 2.X MetaSr 1.0, SE 2.X MetaSr 1.0, .NET CLR 2.0.50727, SE 2.X MetaSr 1.0)",
	"Mozilla/5.0 (iPhone, U, CPU iPhone OS 4_3_3 like Mac OS X, en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
	"MQQBrowser/26 Mozilla/5.0 (Linux, U, Android 2.3.7, zh-cn, MB200 Build/GRJ22, CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"}
func geneAgent() string {
	var r = rand.New(rand.NewSource(time.Now().UnixNano()))
	return userAgent[r.Intn(len(userAgent))]
}

func writeTSV(filename string, store map[string][]string){
	file, err := os.OpenFile("test.csv", os.O_WRONLY|os.O_CREATE, os.ModePerm)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	file.WriteString("\xEF\xBB\xBF") // 写入UTF-8 BOM
	header:=[]string{"href","url","title","link","price","search_comment_num","author"}
	//record:=[]string{href,url,title,link,price,search_comment_num,author}
	writer := csv.NewWriter(file)
	writer.Write(header)
	for _,record :=range store{
		writer.Write(record)
	}
	fmt.Println("文件已经写入"+filename)
}