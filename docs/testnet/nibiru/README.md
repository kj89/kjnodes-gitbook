# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (30)
```bash
peers="07323474e3685dd9ab23c5d515f62ff929c8dab2@45.147.248.163:26656,a3de1f505133b416a47f546b4d4ccbdc442a891b@84.46.251.68:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,8f1a0ff0ca489e1914b032d3f71d9f374187e663@95.217.176.8:26656,bbd9f5419400b8c66b697997945bc7707371e72e@38.242.246.225:26656,26817f6701a7d26ff286533c9fabc3d111ab0cde@149.102.136.186:26656,dfa4419a3d877a9f03f5a73406941fbf2860c6e2@45.140.185.102:26656,cd346200ae861c91da0f90a7a482dc37d09de9a1@185.169.252.139:39656,58a701bc38109860c478e9f5ae5cf6d906190f09@38.242.226.90:26656,d8bc4b3853681bb7012090cb92608d2d5ffb5cfc@38.242.217.41:26656,8279e11d79bb4d5ee3595893a546123423e48b6a@109.123.246.138:26656,39404bc42032805fd570a442918ba65ec4a2ab9e@194.163.171.52:26656,c1ac82cc535c4d260ad074a9f13502cacff415e8@161.97.110.188:26656,687b5fe8f8cf790c79d12dbb40429b91c6f56472@134.209.30.104:26656,7c48ce655af9132d2313e4782904cbb4d204018a@34.28.196.138:39656,b9da17f4f6ae0acd79608006adf04f2929f3cdf4@149.102.136.187:26656,4f357c0ad0eb29ab843577a0d12e15f279899cf4@38.242.226.77:26656,b0c3f66738fb5b2006f8d2ff99ed5a27c1cfc551@84.21.171.146:26656,104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,fae0087a4b4a4692b8e358d7d8cbce75864a7a03@62.171.174.247:26656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,1587dd54b6e1f373ccf61401980816fbd7f7e43a@35.232.147.245:26656,05e99bc295a8318ed7e17b8ac91ac4c1a7be8ca4@38.242.246.190:26656,e068c7e733952e5f10615e1cfba4608a800e4c8c@31.220.93.228:26656,b2a97fa486a00f935753cc406804128170986ef9@38.242.247.232:26656,1c73c34fc319d2944e39442ce93aec707f7f52ef@38.242.242.76:26656,514a6eef19f405d6cb27642d5a93771f2baa460c@194.233.94.138:26656,785ffb99f8724319d44254cbb47b3428aaaa25a5@38.242.236.134:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
