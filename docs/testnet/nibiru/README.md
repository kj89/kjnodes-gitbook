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
peers="7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,b87fb99a9a4b6d2651b4015ff7f055a82ea6acdd@116.202.17.68:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
