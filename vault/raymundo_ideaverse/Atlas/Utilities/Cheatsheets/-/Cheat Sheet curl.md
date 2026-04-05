---
up:
  - "[[Tecnología MOC]]"
created: 2024-07-22
---



# Posting a File with Curl

To post (or upload) a file with Curl, use the -d or -F command-line options and start the data with the @ symbol followed by the file name. To upload multiple files, repeat the -F option several times. Curl will automatically provide the Content-Type header based on the file extension, but you can indicate a custom Content-Type header using the -H command-line option. The file will be sent using the HTTP POST method. You can specify a different HTTP method using the -X command line parameter. For security reasons, ReqBin Online Curl Client does not support sending files from its disk. Click Run to execute the Curl Post File example online and see the results.

Posting a File with Curl [Run](https://reqbin.com/req/c-dot4w5a2/curl-post-file#)

```
curl -d @data.json 
     https://reqbin.com/echo/post/json
```

**Updated**: Jan 12, 2023 **Viewed**: 57722 times

**Author**: [ReqBin](https://reqbin.com/about)

### What is Curl?

[Curl](https://reqbin.com/req/c-r8g2qivg/how-to-use-curl) (stands Client URL) is a command-line tool that runs on [Windows](https://reqbin.com/req/c-g95rmxs0/curl-for-windows), Linux, and macOS [platforms](https://reqbin.com/Article/InstallCurl), designed for transferring data from a server or to a server using many popular network protocols, including [HTTP](https://reqbin.com/Article/HttpProtocol), [HTTPS](https://reqbin.com/req/c-lfozgltr/curl-https-request), and FTP. Curl has built-in support for [SSL](https://reqbin.com/req/c-bw1fsypn/curl-ssl-request), [proxies](https://reqbin.com/req/c-ddxflki5/curl-proxy-server), [certificate validation](https://reqbin.com/req/c-ug1qqqwh/curl-ignore-certificate-checks), [HTTP cookies](https://reqbin.com/req/c-bjcj04uw/curl-send-cookies-example), and user [authentication](https://reqbin.com/Article/HttpAuthentication).

### What is HTTP POST?

[HTTP POST](https://reqbin.com/Article/HttpPost) is the most widely used [HTTP](https://reqbin.com/Article/HttpProtocol) protocol [method](https://reqbin.com/Article/HttpMethods) for sending files and data to a server. The [POST](https://reqbin.com/req/c-g5d14cew/curl-post-example) method asks the web server to accept and process the data contained in the body of the POST message. The POST method is commonly used for uploading files, submitting [HTML forms](https://reqbin.com/req/yjok4snr/post-html-form-example), and [CRUD](https://reqbin.com/Article/CRUDMethods) operations when creating or updating a resource on the server. POST requests can change the server's state and are not idempotent, unlike [GET](https://reqbin.com/Article/HttpGet) and [HEAD request](https://reqbin.com/req/gbfchnr8/head-request-example) methods.

### How to send HTTP POST requests using Curl?

You can send HTTP POST requests using Curl by explicitly specifying the required HTTP method with the -X POST command line parameter. When submitting data using the -d command-line option, Curl automatically selects the HTTP POST method. If you want Curl to use a different HTTP method, such as [HTTP PUT](https://reqbin.com/req/orjagaoq/http-put-request), you can specify this with the -X PUT command-line option.

Curl send POST request example[Run](https://reqbin.com/req/c-dot4w5a2/curl-post-file#)

```curl
curl -X PUT -d '{"id": 1}' https://reqbin.com/echo/post/json
```

  

### How to send a file using Curl?

o upload a file, use the -d command-line option and begin data with the @ symbol. If you start the data with @, the rest should be the file's name from which Curl will read the data and send it to the server.

Curl post file example[Run](https://reqbin.com/req/c-dot4w5a2/curl-post-file#)

```curl
curl -d @path/to/data.json https://reqbin.com/echo/post/json
```

  

Curl will use the file extension to send the correct MIME data type. For example, if you send a JSON file using the command line -d @data.json parameters, Curl will automatically send the Content-Type: application/json HTTP header with your request. If you want to send data with a different type, you can use the -H command-line option and specify your content type.

Send file with a custom Content-Type header example[Run](https://reqbin.com/req/c-dot4w5a2/curl-post-file#)

```curl
curl https://reqbin.com/echo/post/json
   -d @path/to/data.json 
   -H "Content-Type: application/javascript"
```

  

### Curl post file syntax

The general form of the Curl command for posting a file is as follows:

Syntax POST file with Curl

```curl
curl -d @filename [URL]
```

  
Where:

- -d: @filename: file to send to server

### How to upload files with multipart/form-data content type using Curl?

Browsers use the multipart/form-data content type when you upload multiple files to the server via web forms. To submit data with multipart/form-data content type with Curl, use the -F (or --form) command line parameter and precede the parameter value with an @ sign.

Curl submit file with multipart/form-data

```curl
curl -F logo=@filename [URL]
```

  

### What is the difference between the -d and -F options?

The -d command-line option will force Curl to submit data to the server using the **application/x-www-form-urlencoded** format. At the same time, the -F command-line option tells Curl to send data to the server in **multipart/form-data** format.

### How to upload multiple files at once using Curl?

To post multiple files to the server at the same time, add additional -F option for each file name.

Curl upload multiple files

```curl
$ curl [URL]
   -F file1=@filename1
   -F file2=@filename2
   -F file3=@filename3
```

  

### See also

- [How do I send a GET request using Curl?](https://reqbin.com/req/c-1n4ljxb9/curl-get-request-example)
- [How do I send a HEAD request using Curl?](https://reqbin.com/req/c-tmyvmbgu/curl-head-request-example)
- [How to send PUT request using Curl?](https://reqbin.com/req/c-d4os3720/curl-put-example)
- [12 Essential Curl Commands for Linux, Windows and macOS](https://reqbin.com/req/c-kdnocjul/curl-commands)

## Generate Code Snippets for Curl POST File Example

Convert your Curl POST File request to the [PHP](https://reqbin.com/req/php/c-dot4w5a2/curl-post-file), [JavaScript/AJAX](https://reqbin.com/req/javascript/c-dot4w5a2/curl-post-file), [Node.js](https://reqbin.com/req/nodejs/c-dot4w5a2/curl-post-file), [Curl/Bash](https://reqbin.com/req/curl/c-dot4w5a2/curl-post-file), [Python](https://reqbin.com/req/python/c-dot4w5a2/curl-post-file), [Java](https://reqbin.com/req/java/c-dot4w5a2/curl-post-file), [C#/.NET](https://reqbin.com/req/csharp/c-dot4w5a2/curl-post-file) code snippets using the ReqBin code generator.

## Curl POST File Related examples and articles

[How to post JSON using Curl?](https://reqbin.com/req/c-dwjszac0/curl-post-json-example) [How do I post form data using Curl?](https://reqbin.com/req/c-sma2qrvp/curl-post-form-example) [How do I post request body with Curl?](https://reqbin.com/req/c-d2nzjn3z/curl-post-body) [How do I download a file using Curl?](https://reqbin.com/req/c-egazzayq/curl-download-file) [Howto make POST request with basic authentication credentials using Curl?](https://reqbin.com/req/c-2cd3jxee/curl-post-with-basic-authentication-example) [How do I set the content type for a Curl request?](https://reqbin.com/req/c-woh4qwov/curl-content-type) [How do I post XML using Curl?](https://reqbin.com/req/c-yzrfjhug/curl-post-xml-example) [How do I post a request using Curl?](https://reqbin.com/req/c-g5d14cew/curl-post-example) [Top 12 Curl Commands](https://reqbin.com/req/c-kdnocjul/curl-commands)