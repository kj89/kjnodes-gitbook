# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (13)
```bash
peers="8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
