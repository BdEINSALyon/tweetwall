# Social app
## Graphql
### Request example
This request will fetch all published and promoted messages :
```
{
  promoted: allMessages(status: "PR") {
    edges {
      node {
        ...messagesFields
      }
    }
  }
  published: allMessages(status: "PU") {
    edges {
      node {
        ...messagesFields
      }
    }
  }
}

fragment messagesFields on Message {
  id
  text
  image
  video
  videoIsGif
  authorName
  authorUsername
  authorPicture
  publishedAt
  provider {
    type
  }
  providerPostId
  validatedAt
  status
}

```

The response will be like this :
```json
{
  "data": {
    "promoted": {
      "edges": [
        {
          "node": {
            "id": "TWVzc2FnZTox",
            "text": "Hello world ! #foobar",
            "image": "",
            "video": "",
            "videoIsGif": false,
            "authorName": "Foo Bar",
            "authorUsername": "@fbar",
            "authorPicture": "",
            "publishedAt": "2017-02-27T23:39:46+00:00",
            "provider": {
              "type": "TWI"
            },
            "providerPostId": "lel",
            "validatedAt": null,
            "status": "PR"
          }
        }
      ]
    },
    "published": {
      "edges": [
        {
          "node": {
            "id": "TWVzc2FnZToy",
            "text": "L'éclate totale !",
            "image": "https://lel.mdr/lol.png",
            "video": "",
            "videoIsGif": false,
            "authorName": "Foo Bar",
            "authorUsername": "@fbar",
            "authorPicture": "",
            "publishedAt": "2017-02-28T02:24:49+00:00",
            "provider": {
              "type": "TWI"
            },
            "providerPostId": "onche",
            "validatedAt": null,
            "status": "PU"
          }
        }
      ]
    }
  }
}
```
