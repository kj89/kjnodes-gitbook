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
peers="bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,436cb422506a1b3fc9c4e1e5920625e49babe161@185.219.142.214:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,2269d5937ec2b5213ad4ee824ca1ccc328971dc8@185.219.142.179:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,2bfd18d860513e6f0f8c56d4d941b975bf825a50@173.249.7.203:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
