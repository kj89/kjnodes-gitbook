# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/noria.png" alt=""><figcaption></figcaption></figure>

The Noria Network is the only stable-denominated  crypto network. It is envisioned to be the most  accessible and decentralized network for stable money.

**Chain ID**: oasis-3 | **Latest Version Tag**: v1.2.0 | **Wasm**: ON

[Website](https://noria.network) | [Discord](https://discord.gg/pseAWBQ6EZ) | [Twitter](https://twitter.com/NoriaNetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/noria-testnet](https://explorer.kjnodes.com/noria-testnet)

## Public endpoints

* api: [https://noria-testnet.api.kjnodes.com](https://noria-testnet.api.kjnodes.com)
* rpc: [https://noria-testnet.rpc.kjnodes.com](https://noria-testnet.rpc.kjnodes.com)
* grpc: noria-testnet.grpc.kjnodes.com:16190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@noria-testnet.rpc.kjnodes.com:16156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@noria-testnet.rpc.kjnodes.com:16159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/noria-testnet/addrbook.json > $HOME/.noria/config/addrbook.json
```

**live-peers** (11)
```bash
peers="419438c7cb152a88a30d6922a2b2c7077dd4daf5@88.99.3.158:22156,b2b8e67a3158e0854570c7de61812c8c6e92e4bc@65.108.206.118:61656,5eedd8cf7fefc037a6233b1991c2a3b653518560@65.108.230.113:31066,e82fb793620a13e989be8b2521e94db988851c3c@165.227.113.152:26656,4d8147a80c46ba21a8a276d55e6993353e03a734@165.22.42.220:26656,216e01ba9863a27bfe5aecc2ab4d301448a6c6e8@51.79.103.100:26656,38de00b6d88286553eb123d16846190e5c594c59@51.79.30.118:26656,bb04cbb3b917efce76a8296a8411f211bad14352@159.203.5.100:26656,c818c3aa14ae8183578b7be0572c2dcd75613e72@186.233.185.214:26656,846731f7097e684efdd6b9446d562228640e2b14@34.27.228.66:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:16156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noria/config/config.toml
```
