# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (18)
```
peers="7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,1f06a05a88b812f9e8147379a2bb82c8bab37e42@84.46.252.55:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,d6c305ccde3e850ac34228e41952508e48bfa86c@65.21.62.84:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
