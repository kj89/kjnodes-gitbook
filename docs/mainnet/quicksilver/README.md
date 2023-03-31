# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.9-hotfix.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (31)
```bash
peers="4559f4c24037bfad4791b2a6d6d5c769a16cad53@65.109.92.79:15656,ac610f4907efb3e04f4f9915ca3ed91ab0273573@65.108.85.218:26656,679f56feb7f4f91d46a92d0eb474d1dc43466d18@213.239.215.59:29986,3a5d0b97feb595375c24665dcf17d793be129e8b@51.89.155.2:28656,d36921a835076f6d87889793eb05a83099617221@202.61.240.122:26666,ba52d6744d89cf66cf29d7663a21e1299d0f6744@74.80.183.130:26654,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,5e2b0913543b7e1e070e32326d5d901b456b2190@146.19.24.133:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,79b214369c8f52c2d33cf79fc1897677b24cf8cb@94.130.240.229:2000,05241d21ff9e7c699bbdb4faa73da1860b6d8cd7@128.199.85.168:26656,bdbb005129890e3b656841415b3b728d1e4529e6@176.9.155.98:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,0a3860f9d3c27b34910fe8660240ae55699b55c2@84.244.95.245:26656,5f0c0411e34e1c7d0b9c53749d90a923b5e8c625@65.21.133.125:35656,833a368b9e639d50dcbeaa2e8347306979d55e50@199.217.117.78:11156,8ebd6e7c74a9c36a175f9a86148354b378a4f387@185.248.24.16:26656,271419d3eb3878c902ebb0064490ad702d9d067f@144.76.145.150:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,618e09601dd5abb2bd02de957982742e4c1975ab@195.14.6.2:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,58fe3a7b075e7302f8b46b8171a0aa19ff4a427a@65.108.195.29:31126,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,8afd73dde0c073dd290092d8ffbcc48a61c94525@89.117.58.109:46656,063cc6b75194c4f943d32c549667ba210a7f2de1@195.3.222.240:26856,ee14b4bbeb436056952c8e4e7c84826dfb92143b@65.109.105.17:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
