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
peers="04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,bb7c79e9d370dc8ff87c2810f9196aaaa8d9f8ae@65.108.68.119:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036,ce2dcfe5794bed1d4b32b8a43b32afc5d5e435f2@135.181.114.98:46656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,e6eb04d29739ccb134b4c7be12c774a78eb0f875@142.132.148.174:36656,b2dfeee10a366deae4ed6f142d2c99a9dc35577a@109.123.243.187:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,b3a2a298c6a84c503253d120e3eee0c54cea90fd@137.184.193.235:20356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
