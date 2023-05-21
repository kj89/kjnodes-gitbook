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

**live-peers** (12)
```bash
peers="b87fb99a9a4b6d2651b4015ff7f055a82ea6acdd@116.202.17.68:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,c1b40d056e4260a9fa9d1142af1adbeec5039599@142.132.202.50:46656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,2d674121d87cfd1e03654da8fda7ec9f21e46713@65.109.233.78:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
