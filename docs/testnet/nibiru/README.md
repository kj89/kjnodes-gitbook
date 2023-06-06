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

**live-peers** (11)
```bash
peers="b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
