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
peers="3e7ff1b1fa8626812b1ab8acf84a8b60518a8c10@65.109.88.254:34656,785ffb99f8724319d44254cbb47b3428aaaa25a5@38.242.236.134:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,92fafae34fadd3710f1347cbf906b1818ae59f19@185.197.251.86:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,2bfd18d860513e6f0f8c56d4d941b975bf825a50@173.249.7.203:36656,6b76406fb872cc3a4d194c4f0910cf8893f6affb@38.242.148.145:26656,4a44af55ee65d15c13d666bb5d830da43673f7a9@185.190.140.80:26656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,efc2e75111f286ca7117ce4e196bfb7ba29f0a5e@109.123.243.16:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,db832cabda2d29d8e2570c0f3a5797098db5a7b8@135.181.25.101:26656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,4705e330d64ffcc36ef9fe50556f5e44c20a167d@108.61.205.9:26656,b15ff5df6bea62dc567f5b628bb922a4185621b6@5.75.196.224:26656,349a3441e26e7dc8a1d76f69d0acfc820942c837@89.163.215.4:39656,d22160eb98574ecbe437d1009e0f2284110f0626@84.46.254.232:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,76355610ad8576eea4b075e27d7f47799cdc20aa@31.220.82.250:26656,b63dce7de605f933f104b9c2d5102becd2f29509@164.92.138.151:26656,5d55ddb4d498af6062e6e7c0cb7a670aba9b3302@68.183.65.30:26656,8692da09e683b94c0e90a3ce83e4902459c3d044@31.223.32.35:14546,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,e0eeb7517c902ff3ae66acc7383e67b57b572977@38.242.206.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
