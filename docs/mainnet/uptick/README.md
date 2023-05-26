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

**live-peers** (22)
```bash
peers="8d9bfdb1e2657959ec641828080052d554fbe248@65.108.205.47:36656,ee045c74c0678f1122650a3a5223923977cae1b3@65.109.93.152:30656,f9106c0608ff93da93188651ab4b57731b0155be@159.69.73.104:26656,e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,755c376ec8df0c6fce6d3e28f3d9054de4fe456f@81.30.157.35:17656,14ca9d73314dd519bc0b0be8511c88f85fe6873e@46.4.81.204:17656,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,038aca614e49ec4e5e3a06c875976a94c478cb09@65.108.195.29:21656,ffd85619e0baed6ad09eec1e9c1651ded8e00b3b@82.165.186.119:26656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,0720f8f6cd1f1bf1c9549cdb10b920a1583d7675@182.253.224.66:10656,46900f4eb164f31967963544e4d9e7aac0d08a08@107.155.125.186:15656,4914c40a9441895f355c600f38ed94756782ab99@146.59.81.204:27856,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,632c2362378546ab77883077861f38405c378d06@104.194.8.68:60556,bb6aaef7667af68862ee582085c2e9dd2b568d86@54.254.135.200:26656,e88413ee7153be8a9053165a60ad55492a8e300a@65.109.94.250:29656,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,c0b33353fb70d8d71dcb9c8848b3b4207bd56951@188.165.221.155:30598,23e76540bea9b6851b92e280d7e0c123a0d49521@94.23.192.227:30599"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
