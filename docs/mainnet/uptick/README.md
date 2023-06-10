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

**live-peers** (17)
```bash
peers="7ac86e61608b3d44bb0941a8fbb844e5772db984@65.108.69.17:10656,f9106c0608ff93da93188651ab4b57731b0155be@159.69.73.104:26656,21f05f31e3eecf05e3e19c6beb8e53cf1277cce1@94.130.219.37:13656,ea83a93c2878af90d034138fc5026218fb89d0d2@69.197.19.36:21656,e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,e88413ee7153be8a9053165a60ad55492a8e300a@65.109.94.250:29656,b45ee634889abf61c7212b03dbddb853a8a3bc09@185.48.24.112:15656,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,34d28eeb7be1b245fd64ba2df4cdf62b5eb60dd3@202.61.240.155:30001,35e49c8d7af3e6c46ddef3c871768f1d1a112f0f@65.109.88.162:55656,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,4ae1f6e820e5dc33dcb1d1304b8160d25bcc9b0b@89.39.106.78:16656,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,90c0c03d27e5b4354bffb709d28340f2657ca1c7@138.201.121.185:26679"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
