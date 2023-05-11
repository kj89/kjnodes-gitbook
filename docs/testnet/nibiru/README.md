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

**live-peers** (16)
```bash
peers="0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
