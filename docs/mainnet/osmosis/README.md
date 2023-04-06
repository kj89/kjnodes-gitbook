# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,236a60841401f53c28f7609ea50ea88feb259a1e@5.9.100.51:36656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,5bda7b3070d62b4ddbea815e8bea6c6e9548d17d@65.108.140.115:26656,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,677ef9606ea18a13b5dbfad19493d99d7ea068f5@149.56.24.130:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,9bdeb59c97c139187236b2ce92c229c3b9156d93@5.78.80.161:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,d011c34ee72767d7a33d94b79ef158eb49c9a7bf@164.92.70.57:31316,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000,4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,10f328a43a1ac7aeeae7ee34c1127ce6839e4265@15.235.13.139:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,63e4dd6530bf4dc4c2202be256b262a27d661106@146.19.24.108:26656,1a4706c2194cbc055adf4eb89a7b24493bcf33f8@15.235.9.22:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
