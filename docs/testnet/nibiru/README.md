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

**live-peers** (16)
```bash
peers="74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,e1cb0df376c0f88169cb203b304d7cf26b87d1a3@149.102.158.241:26656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,7e75b2249d088a4dfc3b33f386c316cb47366d2b@195.3.221.48:11656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
