# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v10.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:13490

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:13456
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:13459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (9)
```bash
peers="31e7a2eff51ce94def4d04f1e0b361d6e2827fad@169.155.44.206:26656,2eb0e5e53401c51535c13250aba5fe98374ba7f0@51.210.32.145:26656,55c22f83bd9a10213b8b9610627ecd7d49c0a66a@135.181.62.108:26656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,61afb0f37c02031f285f6b27ead2a3e7a97cc28a@35.212.34.104:26656,34f0e424f747f62e04e8c34fde60013fb4dbc04b@65.108.0.165:14956,014c48a6cd4eaa52bc1f58e3a72397e3e5f931b2@34.145.66.159:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
