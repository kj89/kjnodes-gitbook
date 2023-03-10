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

**live-peers** (33)
```bash
peers="7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,bc73e1f3bde267171309e723416690c9c7404881@142.132.199.236:27656,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,6a2e6873ad316bc45342ec3b79430657fe714233@209.97.179.146:26656,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,0d642afa8df369a5021609c43bb7765a332a615f@65.109.106.91:17656,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,decd8ce4d593094c23aace70715291f8a5808da3@212.227.160.56:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
