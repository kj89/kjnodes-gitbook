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

**live-peers** (20)
```bash
peers="b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,7c85671fd863077f7f74d85341beeb53408fae3c@109.123.248.101:26656,85303c3f893e26964b8f5703002e0306c5cd0651@176.57.189.27:34656,efaee8ff19257f93a8bb632aeeec29068e9f39c1@95.214.53.37:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,436cb422506a1b3fc9c4e1e5920625e49babe161@185.219.142.214:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
