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

**live-peers** (29)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,e25aed855f59ad20e44859111f0547be764db21c@154.12.229.17:26656,104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,61f34006e06047850d8be355c62e9ea99bc11a0a@145.40.61.14:26656,c45cde328f28c16b4da3e51c45a64c7ce0c45b1c@93.183.208.71:26656,2d102c50f7a5d35e83761e097f25961eb0880e56@135.181.200.73:26656,1587dd54b6e1f373ccf61401980816fbd7f7e43a@35.232.147.245:26656,01dfe6c993e034169d5e69116e64587fdaf0c2f1@93.183.208.67:26656,a3de1f505133b416a47f546b4d4ccbdc442a891b@84.46.251.68:26656,efc2e75111f286ca7117ce4e196bfb7ba29f0a5e@109.123.243.16:26656,ff8d552e16e96ea49eda07ed0583712b22aa16dd@139.180.154.91:26656,429a1904ebb54d8e9eadeab7a1bd6e9f8797e262@185.182.186.223:26656,4f357c0ad0eb29ab843577a0d12e15f279899cf4@38.242.226.77:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,8279e11d79bb4d5ee3595893a546123423e48b6a@109.123.246.138:26656,efd9203e9c44cb422f6d1bd0046fa458a93c989a@178.74.245.198:26656,a0030987b451e6b196a02eb9c5fc446782397c64@38.242.247.231:26656,a2a6da89a3cf0e1fac01870eac6f6010334c943c@185.190.140.65:39656,58c4f92775bc63621513ce145d58f239aec8c510@89.117.49.71:26656,30abc253688f7e70a6dcae9f0850e41a0245db3a@129.226.148.203:26656,2fa392bd22029266f5ec1631d1f2910f0c9c3163@86.48.5.138:26656,b282548dcf52d4f6fd2ba456635a466c74b88826@184.174.36.198:26656,7635811ac19bde0a542b76a403968ea85fa5f58a@94.250.201.202:26656,09ec1ce2d4d1fc59098bf257c9b848b7d01a8ef3@38.242.225.126:26656,932f77155b5a1989096451eee2b2eb4c1a4bc48a@194.163.191.69:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,d9bea9db5daa0e2be0c2ee9ccda5168fe80f12d3@45.85.249.73:26656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
