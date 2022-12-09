---
description: >-
  Our free Telegram bot is the simpliest way to monitor your Kujira Oracle Feeder health status.
  Get notified when your validator starts to miss Oracle Votes.
---

# Kujira Oracle Monitoring Bot

## Intro

Kjnodes team have created this bot for the <img src="https://github.com/kj89/testnet_manuals/raw/main/pingpub/logos/kujira.png" alt="" data-size="line"> Kujira community to keep validators notified when there is change in Oracle Price Feeder status. When the validator starts to miss Oracle Votes bot will send notification message.

[🤖 Kujira Oracle Monitoring bot | kjnodes](https://t.me/kjnodes\_oracle\_bot)

## How to use

To start using the bot type `/start` command and choose one of the commands:

* :construction\_worker: **Add an operator key** - type in your **valoper** __ address of your validator to add it to the bot.

<figure><img src="../.gitbook/assets/kujira_oracle_bot_menu_add.png" alt=""><figcaption><p>Add an operator</p></figcaption></figure>

* ⭕️ **Reset operator keys** - this will reset all your saved validator entries.
* 📃 **List operator keys** - will list your saved validator entries

<figure><img src="../.gitbook/assets/kujira_oracle_bot_menu_list.png" alt=""><figcaption><p>List of saved operators</p></figcaption></figure>

* 📃 **List all operators** - will list all oracle operators sorted by missed oracle votes in current cycle

<figure><img src="../.gitbook/assets/kujira_oracle_bot_menu_list_all.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To reduce spam alerts with each status change, you will be notified only if your validator exceeds threshold that is set to: **16** missed oracle votes per **10** minutes (That's about **86%** fail ratio)
{% endhint %}

That's it! You are all set! Here is some example of the notification from the bot.

<figure><img src="../.gitbook/assets/kujira_oracle_bot_notification.png" alt=""><figcaption></figcaption></figure>

From kjnodes with :heart:
