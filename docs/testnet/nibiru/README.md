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

**live-peers** (17)
```bash
peers="65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,7f8bd4eaf6b9b213fd7b89ceefc517bcaa517d24@5.9.147.22:22656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,ce2dcfe5794bed1d4b32b8a43b32afc5d5e435f2@135.181.114.98:46656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
