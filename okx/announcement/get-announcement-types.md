## GET / Announcement types

Authentication is not required for this public endpoint.

The response is restricted based on your request IP.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/support/announcement-types`

Request Example

```
GET /api/v5/support/announcement-types
```

#### Request Parameters

None

Response Example

```
{
 "code": "0",
 "data": [
 {
 "annType": "announcements-new-listings",
 "annTypeDesc": "New listings"
 },
 {
 "annType": "announcements-delistings",
 "annTypeDesc": "Delistings"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| annType | String | Announcement type |
| annTypeDesc | String | Announcement type description |
