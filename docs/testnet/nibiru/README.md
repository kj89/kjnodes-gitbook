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

**live-peers** (41)
```bash
peers="049dea10cadfb78ec5e7605809fe5c868e372ab5@149.28.126.247:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656,5eecfdf089428a5a8e52d05d18aae1ad8503d14c@65.108.141.109:19656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,9886bde397f0aaf4c9402e618b49393746266c3a@62.141.39.134:26656,2a11b3e06f832e430efb41e3c3bb07a42875d20c@154.53.34.112:26657,d2b6baed49aa475eb6ec5958bfbca30a61363b86@154.53.52.212:26657,0d7d4f9b5dfe2dcc9c313fa3695eacd22e132a1b@125.111.119.12:26657,cf29df0bc1d8a1d9053d7dc6bd7b8ee69b3021cc@51.89.47.31:26656,72a84166fbd6b92d8a772843026cf6a2cd97ffbe@65.109.60.19:46656,2d953905edc0eeadad8f70a7ead6a6bba327c0ce@173.212.216.232:12656,371970df586e85414231fc1b530bde1c65116e71@65.108.76.44:11733,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,719e5c2c79f027c65514d70e0f08d754119a6f0c@45.10.154.246:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,bfd1670d642542ff1213b33dd6fb5db1769a17e8@185.234.69.143:26656,c7f3b61275dc16993c39a1ebc9f6cb5895d11d56@148.251.43.226:15656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,b1b38341e4d443e2b8d97368c734c1578e4f01cb@46.151.27.109:39656,ff60133778ab80489636a81ec861b508e6d6aca4@34.168.169.45:26656,334af61b52388924e3a1c6ac1af57ffbac2ad752@84.46.255.14:26656,cfddc0756f937110aedf1acaffa4527f549f720d@78.29.44.119:36656,ab5a794451f4b19055300f692160f4f20d55a891@82.208.21.81:26656,438701ce016699880f9073c6b99f71d17309d820@154.53.52.215:26657,694ef36622642377aec8847df309d1dec708cb28@195.201.197.4:38656,60cccfd84d17c94f17de82480ce48a1da0bf8234@135.181.16.252:34656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,0c3c0b937a1f8054794cacd744bf1a13b341508b@113.53.82.252:36656,aa882f345fd3febd66f0693d4525a537bdaa35ec@194.233.67.92:39656,0348b1eaa2c137c3680767c2955df9f1ebcd58de@65.108.234.126:17656,dd67c1fb79d23a4a2f61fa85f6ed2d27ec6ad69a@168.119.227.28:29656,e579409f763fb945569c8d04f0f3257607ab88af@38.242.242.23:26656,e58e450d695a286ac32ae52d2f588e725f81abe4@185.241.151.142:26656,32c587c3d9329e6c13c5cd7797eb46b30b628bca@91.107.132.237:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
