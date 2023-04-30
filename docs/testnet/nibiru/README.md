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

**live-peers** (25)
```bash
peers="ac0bfac1e3173dbbf995b1690172e514143bbe63@65.109.86.216:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,736acf4bea85fc40b63093f018805e03c989bcce@75.119.143.229:26656,7c85671fd863077f7f74d85341beeb53408fae3c@109.123.248.101:26656,acf3a54a0b38a88a2ae0d41060e72842dcf24d63@195.2.70.48:26656,345cfe2a2081fee1788ee54fbb106be4900c0294@148.251.10.110:27060,7635811ac19bde0a542b76a403968ea85fa5f58a@94.250.201.202:26656,d00cdd120096a5464984f29ec360f720677da2fe@89.116.24.30:39656,7685c50934491640cc4c082a687d4d7c140a0816@38.242.226.1:26656,4432207b04118601f777ac93a5c3dd441b968734@70.34.250.4:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,19fd0e304b15b5ce7abbbf27779eac77ca08fc23@65.109.157.236:46656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,c2c6a9d863ba70697553b5b34f17393153ee16c2@38.242.226.87:26656,58d0515248ac43967a7a7c3e136023d55e2a5d4f@109.123.240.111:26656,acecf3fc06e98262607282699f389eb30d2cdb89@89.116.30.166:26656,db1deb2f4d23eb91da1d10e86562d84aaa0f9a0e@5.75.239.226:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
