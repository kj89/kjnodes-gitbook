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

**live-peers** (30)
```bash
peers="dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,46cd4ab1a4fd92ee0ab510d05dce3cd00e639a05@3.235.146.125:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,a9123ae1e1b7f8438e7262efd50031aab600df41@154.12.225.160:32656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,f2994f0ed16756151914ee95f041a7bff4f82b22@138.201.204.5:29656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
