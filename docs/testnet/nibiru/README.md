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

**live-peers** (19)
```bash
peers="668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
