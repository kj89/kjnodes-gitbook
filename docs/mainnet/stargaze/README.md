# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stargaze.png" alt=""><figcaption></figcaption></figure>

Stargaze is a Cosmos zone (layer 1 proof-of-stake blockchain).  It is the base layer node software for the Stargaze NFT Marketplace.

**Chain ID**: stargaze-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: ON

[Website](https://www.stargaze.zone) | [Discord](https://discord.gg/stargaze) | [Twitter](https://twitter.com/stargazezone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/stargaze](https://explorer.kjnodes.com/stargaze)

## Public endpoints

* api: [https://stargaze.api.kjnodes.com](https://stargaze.api.kjnodes.com)
* rpc: [https://stargaze.rpc.kjnodes.com](https://stargaze.rpc.kjnodes.com)
* grpc: stargaze.grpc.kjnodes.com:15890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stargaze.rpc.kjnodes.com:15856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stargaze.rpc.kjnodes.com:15859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stargaze/addrbook.json > $HOME/.starsd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="fc668bbf7e34d6926308487348b2655159198f1d@135.181.128.114:13756,15bf6fc85e4e37b2c96e35c7b76816670ad63c18@65.108.75.107:8656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.235:26656,778e22fa6e604e9fdd410c2ef9598254eb34f46a@198.244.176.186:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15856,0d9c5b7b4361cacb7ec5b08b818358f9cf23034b@65.108.66.92:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.11:26656,9125aeea6976e9550fd824a8ff517d1f0dca06d5@95.214.53.201:26656,c2054e53fdb2f5cafb1a2f633de064143c16057c@93.189.30.126:26656,9c948410d4a8483ada2dc4184fbc8f7121ed0c1a@51.89.7.185:26629"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.starsd/config/config.toml
```
