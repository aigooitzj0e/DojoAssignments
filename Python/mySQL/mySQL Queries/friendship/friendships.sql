SELECT * FROM users
LEFT JOIN friendships ON users_id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id