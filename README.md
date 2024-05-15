
## API Reference

#### Registering New Account

```http
POST /api/auth/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. your email address |
| `password` | `string` | **Required**. your password |
| `username` | `string` | **Required**. your username |

#### Loging In To An Account

```http
POST /api/auth/login/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`      | `string` | **Required**. your email address |
| `password`      | `string` | **Required**. your password |

#### Refreshing JWT Token

```http
POST /api/auth/token/refresh/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**. your JWT token |


#### Getting A User

```http
GET /api/auth/users/${username}/
```


#### Generating New Blog

```http
POST /api/generate/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `link`      | `string` | **Required**. youtube video link |


#### Getting User's Blog

```http
GET /api/my-blogs/
```

Header Parameter:
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | **Required**. Bearer 'your JWT token' |

#### Getting All Blogs

```http
GET /api/blogs/
```

#### Getting Single Blog

```http
GET /api/blogs/${blogId}
```
