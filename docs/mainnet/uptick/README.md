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

**live-peers** (20)
```bash
peers="f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,1160d5e94fbce4f8ccabb0203344c673f3af3fb6@141.94.139.233:27656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,7ac86e61608b3d44bb0941a8fbb844e5772db984@65.108.69.17:10656,bb6aaef7667af68862ee582085c2e9dd2b568d86@54.254.135.200:26656,250c98d4975ae9a12ed7dfcd5a7cf76b470e49a6@65.21.108.180:26656,8ecd3260a19d2b112f6a84e0c091640744ec40c5@185.165.241.20:26656,755c376ec8df0c6fce6d3e28f3d9054de4fe456f@81.30.157.35:17656,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,ffd85619e0baed6ad09eec1e9c1651ded8e00b3b@82.165.186.119:26656,0720f8f6cd1f1bf1c9549cdb10b920a1583d7675@182.253.224.66:10656,169fd4bb8dee17a0cd8d3747788b3cdac2dbb137@171.247.172.188:35656,14ca9d73314dd519bc0b0be8511c88f85fe6873e@46.4.81.204:17656,632c2362378546ab77883077861f38405c378d06@104.194.8.68:60556,7a320021212d346a7e8bfd5926feb4b307e7f69b@5.9.147.22:26556,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,8e924a598a06e29c9f84a0d68b6149f1524c1819@57.128.109.11:26656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30598"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
