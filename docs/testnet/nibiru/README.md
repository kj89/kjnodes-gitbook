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

**live-peers** (13)
```bash
peers="a5455fdd70a915023bb4902143704430793c3e68@162.55.163.78:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,db832cabda2d29d8e2570c0f3a5797098db5a7b8@135.181.25.101:26656,e3fc96a180861a923807d29b748a6cddd3230a8f@5.189.171.168:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,5160aa16c18a37d25c3e667c80de83279715f2aa@195.2.75.252:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,fee8c13c90bc44816ad3b6dbca1d1044008b1b87@65.21.106.157:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
