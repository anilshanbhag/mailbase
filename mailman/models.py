from django.db import models
from django.contrib.auth.models import User

  # $lfnkwnf="email";$eblkgkdfjuk="q2";${${"GLOBALS"}["udspvkdbuil"]}="CREATE TABLE `apps` (
  #       `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  #       `userID` int(11) DEFAULT NULL,
  #       `app_name` varchar(100) DEFAULT NULL,
  #       `from_name` varchar(100) DEFAULT NULL,
  #       `from_email` varchar(100) DEFAULT NULL,
  #       `reply_to` varchar(100) DEFAULT NULL,
  #       PRIMARY KEY (`id`)
  #     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

# class App(models.Model):
#   user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
#   app_name = models.TextField()
#   from_name = models.TextField()
#   from_email = models.TextField()
#   reply_to = models.TextField()

  #   ";${$eblkgkdfjuk}="CREATE TABLE `campaigns` (
  #       `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  #       `userID` int(11) DEFAULT NULL,
  #       `app` int(11) DEFAULT NULL,
  #       `from_name` varchar(100) DEFAULT NULL,
  #       `from_email` varchar(100) DEFAULT NULL,
  #       `reply_to` varchar(100) DEFAULT NULL,
  #       `title` varchar(500) DEFAULT NULL,
  #       `plain_text` mediumtext,
  #       `html_text` mediumtext,
  #       `sent` varchar(100) DEFAULT '',
  #       `recipients` int(100) DEFAULT '0',
  #       `opens` longtext,
  #       `wysiwyg` int(11) DEFAULT '0',
  #       PRIMARY KEY (`id`)
  #     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

class Campaign(models.Model):
  # user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
  # app = models.ForeignKey(App, db_index=True, on_delete=models.CASCADE)
  from_name = models.CharField(max_length=100, default=None)
  from_email = models.CharField(max_length=100, default=None)
  reply_to = models.CharField(max_length=100, default=None)
  title = models.TextField()
  plain_text = models.TextField()
  html_text = models.TextField()
  # time_condition = models.CharField(max_length=100, default=None)
  # timezone = models.CharField(max_length=100, default=None)
  # created = models.IntegerField(max_length=11, default=None)
  recipients = models.IntegerField(default=0)
  opens = models.TextField()
  wysiwyg = models.IntegerField(default=0)

  #   ";${"GLOBALS"}["biaxbmtqkbh"]="q5";$ivtqhsfocof="license";$bmshddsbxij="mysqli";${${"GLOBALS"}["lnnqehlgv"]}="CREATE TABLE `links` (
  #       `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  #       `campaign_id` int(11) DEFAULT NULL,
  #       `link` varchar(1500) DEFAULT NULL,
  #       `clicks` longtext,
  #       PRIMARY KEY (`id`)
  #     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
class Link(models.Model):
  campaign = models.ForeignKey(Campaign, db_index=True, on_delete=models.CASCADE)
  link = models.TextField()
  clicks = models.TextField()

  #   ";$msemaohzco="license";${"GLOBALS"}["rfmtrnf"]="aws_key";$gjuopqq="mysqli";$rglwspb="timezone";$cdnozekpvx="pass_encrypted";${${"GLOBALS"}["itoouycnaicf"]}="CREATE TABLE `lists` (
  #       `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  #       `app` int(11) DEFAULT NULL,
  #       `userID` int(11) DEFAULT NULL,
  #       `name` varchar(100) DEFAULT NULL,
  #       PRIMARY KEY (`id`)
  #     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
class List(models.Model):
  # app = models.ForeignKey(App, db_index=True, on_delete=models.CASCADE)
  name = models.TextField()

  #   ";$lxwttnv="mysqli";${${"GLOBALS"}["biaxbmtqkbh"]}="CREATE TABLE `login` (
  #       `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  #       `name` varchar(100) DEFAULT NULL,
  #       `company` varchar(100) DEFAULT NULL,
  #       `username` varchar(100) DEFAULT NULL,
  #       `password` varchar(500) DEFAULT NULL,
  #       `s3_key` varchar(500) DEFAULT NULL,
  #       `s3_secret` varchar(500) DEFAULT NULL,
  #       `api_key` varchar(500) DEFAULT NULL,
  #       `license` varchar(100) DEFAULT NULL,
  #       `timezone` varchar(100) DEFAULT NULL,
  #       PRIMARY KEY (`id`)
  #     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

class Login(models.Model):
  name = models.TextField()
  s3_key = models.TextField()
  s3_secret = models.TextField()
  api_key = models.TextField()

  #   ";${${"GLOBALS"}["mapznmvfqby"]}="CREATE TABLE `subscribers` (
  #       `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  #       `userID` int(11) DEFAULT NULL,
  #       `name` varchar(100) DEFAULT NULL,
  #       `email` varchar(100) DEFAULT NULL,
  #       `list` int(11) DEFAULT NULL,
  #       `unsubscribed` int(11) DEFAULT '0',
  #       `bounced` int(11) DEFAULT '0',
  #       `last_campaign` int(11) DEFAULT NULL,
  #       `timestamp` int(100) DEFAULT NULL,
  #       PRIMARY KEY (`id`)
  #     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
  #   ";
class Subscriber(models.Model):
  user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
  list = models.ForeignKey(List, db_index=True, on_delete=models.CASCADE)
  unsubscribed = models.IntegerField(default = 0)
  bounced = models.IntegerField(default = 0)
  last_campaign = models.IntegerField(default = 0)
  timestamp = models.DateTimeField(auto_now_add = True)

  # s3_key = models.TextField()
  # s3_secret = models.TextField()
  # api_key = models.TextField()

class Template(models.Model):
  # user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
  # app = models.ForeignKey(App, db_index=True, on_delete=models.CASCADE)
  template_name = models.CharField(max_length=100, default=None)
  html_text = models.TextField()

# class BlockedDomain(models.Model):
#   # app = models.ForeignKey(App, db_index=True, on_delete=models.CASCADE)
#   domain = models.TextField()
#   timestamp = models.DateTimeField(auto_now_add = True)
#   block_attempts = models.IntegerField(default=0)

# class Ares(models.Model):
#     name = models.CharField(max_length=100, default=None)
#     type = models.IntegerField(default = 0)
#     list = models.IntegerField(default = 0)
#     custom_field = models.CharField(max_length=100, default=None)

# class AresEmails(models.Model):
#     ares = models.ForeignKey(Ares, on_delete=models.CASCADE)
#     from_name = models.CharField(max_length=100, default=None)
#     from_email = models.CharField(max_length=100, default=None)
#     reply_to = models.CharField(max_length=100, default=None)
#     title = models.TextField()
#     plain_text = models.TextField()
#     html_text = models.TextField()
#     time_condition = models.CharField(max_length=100, default=None)
#     timezone = models.CharField(max_length=100, default=None)
#     created = models.IntegerField(max_length=11, default=None)
#     recipients = models.IntegerField(max_length=100, default=0)
#     opens = models.TextField()
#     wysiwyg = models.IntegerField(max_length=11, default=0)

# class Queue(models.Model):
#     query_str = models.TextField()
#     campaign_id = models.IntegerField(max_length=11, default=None)
#     subscriber_id = models.IntegerField(max_length=11, default=None)

# # Not needed
# class Zapier(models.Model):
#     subscribe_endpoint = models.CharField(max_length=100, default=None)
#     event = models.CharField(max_length=100, default=None)
#     list = models.IntegerField(max_length=11, default=None)
#     app = models.IntegerField(max_length=11, default=None)

# class Seg(models.Model):
#     name = models.CharField(max_length=100, default=None)
#     app = models.IntegerField(max_length=11, default=None)
#     list = models.IntegerField(max_length=11, default=None)
#     last_updated = models.CharField(max_length=100, default=None)

# class SegCons(models.Model):
#     seg_id = models.IntegerField(max_length=11, default=None)
#     grouping = models.IntegerField(max_length=11, default=None)
#     operator = models.CharField(max_length=3, default=None)
#     field = models.CharField(max_length=100, default=None)
#     comparison = models.CharField(max_length=11, default=None)
#     val = models.CharField(max_length=500, default=None)

# class SubscribersSeg(models.Model):
#     seg_id = models.IntegerField(max_length=11, default=None)
#     subscriber_id = models.IntegerField(max_length=11, default=None)

# class SuppressionList(models.Model):
#     app = models.IntegerField(max_length=11, default=None)
#     email = models.CharField(max_length=100, default=None)
#     timestamp = models.CharField(max_length=100, default=None)
#     block_attempts = models.IntegerField(max_length=100, default=0)

# class BlockedDomains(models.Model):
#     app = models.IntegerField(max_length=11,default=None)
#     domain = models.CharField(max_length=100,default=None)
#     timestamp = models.CharField(max_length=100,default=None)
#     block_attempts = models.IntegerField(max_length=100,default=0)

# class SkippedEmails(models.Model):
#     app = models.IntegerField(max_length=11,default=None)
#     list = models.IntegerField(max_length=11,default=None)
#     email = models.CharField(max_length=100,default=None)
#     reason = models.IntegerField(max_length=1,default=None)

