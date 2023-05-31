# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" alt=""><figcaption></figcaption></figure>

Uptick Network is building business-grade infrastructure and  ecosystems for non-fungible tokens (NFTs). The platform is  designed with a focus on multi-chain and cross-chain interoperability,  and includes three key components: the NFT infrastructure, an NFT  marketplace, and NFT ecosystem applications.

**Chain ID**: uptick_117-1 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/uptick/uptickvaloper1jqpaf0vgzlxvjx5meq8huweuv2nguqe20seefq)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/uptick/uptickvaloper1jqpaf0vgzlxvjx5meq8huweuv2nguqe20seefq) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/uptick](https://explorer.kjnodes.com/uptick)

## Public endpoints

* api: [https://uptick.api.kjnodes.com](https://uptick.api.kjnodes.com)
* rpc: [https://uptick.rpc.kjnodes.com](https://uptick.rpc.kjnodes.com)
* grpc: uptick.grpc.kjnodes.com:11590

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@uptick.rpc.kjnodes.com:11556
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@uptick.rpc.kjnodes.com:11559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (16)
```bash
peers="f9106c0608ff93da93188651ab4b57731b0155be@159.69.73.104:26656,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,1160d5e94fbce4f8ccabb0203344c673f3af3fb6@141.94.139.233:27656,14ca9d73314dd519bc0b0be8511c88f85fe6873e@46.4.81.204:17656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,5f371e4c7e40292fdc4bfc9f092798db55263aee@65.109.88.162:15656,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,755c376ec8df0c6fce6d3e28f3d9054de4fe456f@81.30.157.35:17656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,ffd85619e0baed6ad09eec1e9c1651ded8e00b3b@82.165.186.119:26656,e88413ee7153be8a9053165a60ad55492a8e300a@65.109.94.250:29656,250c98d4975ae9a12ed7dfcd5a7cf76b470e49a6@65.21.108.180:26656,b2bcb66f270153791b19e16ff23ddfec096f7097@142.132.202.50:41656,bb6aaef7667af68862ee582085c2e9dd2b568d86@54.254.135.200:26656,632c2362378546ab77883077861f38405c378d06@104.194.8.68:60556,34d28eeb7be1b245fd64ba2df4cdf62b5eb60dd3@202.61.240.155:30001"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
