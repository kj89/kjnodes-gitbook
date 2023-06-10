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
peers="cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,c1b40d056e4260a9fa9d1142af1adbeec5039599@142.132.202.50:46656,954598490831bce4e650593d23466bf676c04914@185.16.39.19:38656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
