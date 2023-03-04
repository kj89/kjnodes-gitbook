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
peers="e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,b731df187ce2b278b60bc3469e13c6bac278dcc9@167.235.139.212:26656,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,46cd4ab1a4fd92ee0ab510d05dce3cd00e639a05@3.235.146.125:26656,6ac8cfef2cabd1b2f4158c3d6709815f1e1ca0db@91.225.162.243:26656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,f2994f0ed16756151914ee95f041a7bff4f82b22@138.201.204.5:29656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,6a2e6873ad316bc45342ec3b79430657fe714233@209.97.179.146:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
