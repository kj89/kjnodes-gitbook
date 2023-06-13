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
peers="bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,ba49814ebe24e4d1ba41f4fc774997bd5d7d8e47@65.108.126.46:35656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
