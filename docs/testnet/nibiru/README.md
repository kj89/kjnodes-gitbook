# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-2 | **Latest Version Tag**: v0.16.3 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (27)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,507e09ffa4899d931de427fd7747c34f46cfb5ab@95.216.156.7:26656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,911a6a9a932f21326e4947d492ff03c405e9039e@65.109.86.236:27656,b57a9c1e7c0f597c9ef6a47cc361094f95a22b84@192.9.134.157:27656,99b57896e917866956f9f078f67f95d6fd6a05e8@161.97.92.139:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,98032241ea61ca6ac066b8fa508baace6678a7a3@190.2.155.67:31656,72a84166fbd6b92d8a772843026cf6a2cd97ffbe@65.109.60.19:46656,ffcade6628819c7934399f7d7a03a25d6c7ef281@75.119.130.237:26656,f12288a1ed3a9da2c609763be79a0e5bd00e1fb7@167.86.80.145:39656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,0c3c0b937a1f8054794cacd744bf1a13b341508b@113.53.82.252:36656,694ef36622642377aec8847df309d1dec708cb28@195.201.197.4:38656,2d953905edc0eeadad8f70a7ead6a6bba327c0ce@173.212.216.232:12656,2f194c30648649e0d8b311f68fdd0baa58896445@161.97.136.141:26656,a050a5016c8c01bb97debb5b4730edd239c6a8a4@92.38.241.228:26656,e4ea6ffd9ec8ca5db91506e0429613628f0f61ee@155.133.22.115:26656,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,d76ac9af962fe6d00766baa2bdf1c7aa61e2d634@217.76.60.115:26656,52dacee88cf2b6dc8f6e2c1876880bf370796e72@185.219.142.214:39656,85ea7dbcf6c0f35bdb42fb645ce579d9438ed76e@88.99.13.85:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,6b79cd4cadd1590367ff87311d87a1eec0491b6f@212.86.102.214:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
