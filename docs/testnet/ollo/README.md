# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)




## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: [https://ollo-testnet.grpc.kjnodes.com](https://ollo-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (32)
```bash
peers="412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,ef2b392423003fe81c92ff8de2d08febc19b220e@142.93.36.7:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,b731df187ce2b278b60bc3469e13c6bac278dcc9@167.235.139.212:26656,771cfca799033e327511b25ae77784e02818d77f@65.108.101.4:23486,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,f2994f0ed16756151914ee95f041a7bff4f82b22@138.201.204.5:29656,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,e709b708ea24ed8fefb5c82cc460bb485b403960@83.25.243.187:28656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
