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

**live-peers** (27)
```bash
peers="104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,c45cde328f28c16b4da3e51c45a64c7ce0c45b1c@93.183.208.71:26656,8279e11d79bb4d5ee3595893a546123423e48b6a@109.123.246.138:26656,fc015be87e5c15953a6508403c99a6c8d9493622@194.34.232.35:39656,64fc57fb297ef839da5212b391cf27b32fe7ab8a@109.123.243.55:26656,1587dd54b6e1f373ccf61401980816fbd7f7e43a@35.232.147.245:26656,fae0087a4b4a4692b8e358d7d8cbce75864a7a03@62.171.174.247:26656,a3de1f505133b416a47f546b4d4ccbdc442a891b@84.46.251.68:26656,6dbb917a5a8d263ccaf2ef33d957116225b19e67@31.220.88.184:26656,549ba520c02bf82dd4198cddde2927ca5a574a9a@84.46.247.207:26656,997c1e7fb9b7e6cfa6092b4fe09a0f3ed1907781@65.21.2.131:26656,08a1222c47c36bbd31bc693fe625026a275566e6@38.242.254.154:26656,9e31682ed08dd4d5e9662dd9fd3c42b06f50c6d8@109.123.243.107:26656,4f8d3dec691e8cbf20883cf595a9a0e749178bdb@65.108.229.93:27656,f328de4ff3f71b14882fc08c6793bfa272cd7171@45.85.249.93:26656,2137cde84a36e8e0cf17230c58670034096d3798@138.201.200.252:26656,b15ff5df6bea62dc567f5b628bb922a4185621b6@5.75.196.224:26656,3b5c0147311c294de8e635c853af5a0de72d43f1@65.21.131.215:26566,1f910c413b5e098fa9c2d066d405b1f87b0a32c6@113.23.122.67:26656,de9410cc356635b1f555c06332af943319b75a80@109.123.243.29:26656,f883b1634fd918b036176fc12976194b4bc775af@38.242.205.150:39656,7bb000363922f1da93c0f25b2544e453b523a82a@65.108.246.178:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,4cf0fe54e468cb18fc2d5cca41dcc387e8c8de5c@91.233.173.45:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
