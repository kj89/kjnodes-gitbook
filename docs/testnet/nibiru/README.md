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
peers="4a44af55ee65d15c13d666bb5d830da43673f7a9@185.190.140.80:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,99cb951f06e17236c89cb5ba54aec105720d0228@38.242.158.5:26656,619efff2a2f4752acc99ff6fff45c34299cacdbb@85.239.232.209:26656,a6f5122468d51e393c2902faf7d15120326b9a7b@178.92.89.24:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,7548759ac2ad3e4eb2f7427899b451b360f4f8a2@65.21.204.190:26656,9599e32760a56ac27d4a354c167c7b18e2362438@185.197.251.85:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,7b69fec8f71ccb56b0a2d7ddc07a92c2982a77d1@34.125.91.236:26656,c36bcb5907e0ac74018bf42982b249be090e92c1@192.248.150.77:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,efc2e75111f286ca7117ce4e196bfb7ba29f0a5e@109.123.243.16:26656,e9c2b31f877ffe56597e68898f113797719b57e6@65.21.240.20:39656,5d55ddb4d498af6062e6e7c0cb7a670aba9b3302@68.183.65.30:26656,d191900c45d3df1611aa48c1a3bf24f851dc25c6@165.227.155.35:26656,6551db4af9ddf233e4b83182f57488c25f691d70@38.242.153.29:26656,697c14302048b65f1e292a10632bda307cb6a149@38.242.199.224:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,041494f82ba6107b05d5f1c5ea3d8e024c479480@31.220.83.9:26656,8279e11d79bb4d5ee3595893a546123423e48b6a@109.123.246.138:26656,e3bcf7faf6efca24f6d0735bc96f67929a8164d3@164.90.217.176:26656,65540cd7344f08eb6ae3144f21500ad22f5778cd@45.88.223.42:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
