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

**live-peers** (18)
```bash
peers="7ac86e61608b3d44bb0941a8fbb844e5772db984@65.108.69.17:10656,e88413ee7153be8a9053165a60ad55492a8e300a@65.109.94.250:29656,07933f8021f92499457890184ae228cd4a2a52fb@65.21.90.141:26656,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,29269b318b35005b4ac39d010cbc3c41a5ab0833@185.144.99.33:26656,755c376ec8df0c6fce6d3e28f3d9054de4fe456f@81.30.157.35:17656,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,8d9bfdb1e2657959ec641828080052d554fbe248@65.108.205.47:36656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,34d86f3a8dfce7d8b615563c587433c65792f104@185.219.142.221:15656,90c0c03d27e5b4354bffb709d28340f2657ca1c7@138.201.121.185:26679,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,34d28eeb7be1b245fd64ba2df4cdf62b5eb60dd3@202.61.240.155:30001,b2bcb66f270153791b19e16ff23ddfec096f7097@142.132.202.50:41656,024a9c6eb41193e7fc76544572c0a8370e80e953@65.109.92.240:3156,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@142.132.148.140:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
