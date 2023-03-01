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

**live-peers** (26)
```bash
peers="47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,b731df187ce2b278b60bc3469e13c6bac278dcc9@167.235.139.212:26656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,427c72976f11fc183c839b07026804119454915b@68.183.125.58:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
