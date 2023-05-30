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

**live-peers** (10)
```bash
peers="73e5dc6e04a1dd28e5851191eb9dede07f0b38fb@141.94.99.87:14095,b2b8e67a3158e0854570c7de61812c8c6e92e4bc@65.108.206.118:61656,f60568a6ed1f848857c1c6c113719c1bb687c656@65.108.105.48:22156,5eedd8cf7fefc037a6233b1991c2a3b653518560@65.108.230.113:31066,216e01ba9863a27bfe5aecc2ab4d301448a6c6e8@51.79.103.100:26656,e82fb793620a13e989be8b2521e94db988851c3c@165.227.113.152:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:16156,38de00b6d88286553eb123d16846190e5c594c59@51.79.30.118:26656,c818c3aa14ae8183578b7be0572c2dcd75613e72@186.233.185.214:26656,31df60c419e4e5ab122ca17d95419a654729cbb7@102.130.121.211:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noria/config/config.toml
```
