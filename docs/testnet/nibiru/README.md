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

**live-peers** (14)
```bash
peers="c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,072975554bef679c2fa798e0e29b7606c2c20073@38.242.248.93:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,2bfd18d860513e6f0f8c56d4d941b975bf825a50@173.249.7.203:36656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,c20a499a21668237d67b44d44623aaebedbea81f@173.249.20.170:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
