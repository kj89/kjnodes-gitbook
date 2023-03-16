# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)




## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: ollo-testnet.grpc.kjnodes.com:32090

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

**live-peers** (35)
```bash
peers="67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,decd8ce4d593094c23aace70715291f8a5808da3@212.227.160.56:28656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,caed81ae44835c12c73954b8844e6c4fc8d1b781@161.35.170.17:32656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,0f99f7481a1b49701866ddbdfe71dc3b2fd792d8@109.123.244.56:26626,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
