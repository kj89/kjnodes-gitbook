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
peers="e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d68895141d74eadfb1b620955102ad2db6b1d9ea@51.195.88.136:15662,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,2d674121d87cfd1e03654da8fda7ec9f21e46713@65.109.233.78:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
