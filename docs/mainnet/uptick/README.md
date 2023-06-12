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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11556,024a9c6eb41193e7fc76544572c0a8370e80e953@65.109.92.240:3156,a5408575fc327823f73c153d9f89c932ac30a335@141.94.141.144:28056,21f05f31e3eecf05e3e19c6beb8e53cf1277cce1@94.130.219.37:13656,ea83a93c2878af90d034138fc5026218fb89d0d2@69.197.19.36:21656,90c0c03d27e5b4354bffb709d28340f2657ca1c7@138.201.121.185:26679,f05733da50967e3955e11665b1901d36291dfaee@65.108.195.30:21656,f9106c0608ff93da93188651ab4b57731b0155be@159.69.73.104:26656,e71bae28852a0b603f7360ec17fe91e7f065f324@142.132.253.112:35656,81ccbba5cba98cf89bcca74f271380b53afed4c4@154.26.130.207:27656,f2710fe78495a0645b690dbf9296b5d62bc2a39f@148.113.6.229:20456,8d9bfdb1e2657959ec641828080052d554fbe248@65.108.205.47:36656,46900f4eb164f31967963544e4d9e7aac0d08a08@107.155.125.186:15656,8ef5753cf3feba8f931ca771575d353556073e81@194.163.172.190:26656,7a320021212d346a7e8bfd5926feb4b307e7f69b@5.9.147.22:26556,b2bcb66f270153791b19e16ff23ddfec096f7097@142.132.202.50:41656,169fd4bb8dee17a0cd8d3747788b3cdac2dbb137@171.247.172.188:35656,d61b985df3c9f2e11f47784e88b11a920a041638@195.201.197.4:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
