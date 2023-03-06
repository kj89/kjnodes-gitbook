# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

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

**live-peers** (42)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d6207476a91813659a21b5a14479015aa3b3640b@34.125.57.58:18656,e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,fd318fe2c3a80e957a7900531a3822a9515f6c19@159.69.72.220:26656,0bc611c38f435f2f2b8d2377a90147564d4a80fe@185.234.69.143:26656,6ad350ae8f3713c37f4afc24f4b6c93ed7fd3c58@185.207.251.165:26656,9f06819b9ca5927310ffad266220ec2b1c2a0edc@82.165.207.203:39656,68ae83dd208d835c30059f24705423c9c46ebba9@188.127.253.221:46656,a37f72e68e61b0dfbe01e7509753d27c5dc54ec9@157.245.148.64:39656,5b2d7ccdf924ff16c3d0e3b55c4547a71c99dc42@161.97.122.167:39656,6fefa7ece2ff81d1c228c31eda72692d9299d8bc@38.242.248.145:26656,a7d54a2b6657f13de1d82dbd69a4dc4d0289d4cc@217.76.63.110:26656,b6db16ab4d2dfd61d0be94df4738ce5f1913de11@212.41.9.98:26656,1750291aa1de3b04f07161ad4c0f2a47e7879d63@65.21.63.46:26656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,a0b043d6c1c0f77d11f70ddcf78b753bb94f1642@167.86.117.179:26656,a03eaa525bd984d713fd9b000a89163dc7516a83@185.207.250.222:26656,46b2205032ff6f15ce8cdca7d225aca3d84db47d@45.85.146.7:39656,39dfeaa1cc3fda73074ec6cd92750a7076e5c2f9@194.163.181.0:26656,f2b77362c141f846c0bd8f795895bfe60589eaa7@185.237.96.110:26656,5ae4c8cc5763de7c105dd3dba66b7212328bced5@23.248.175.210:26656,57cd99659f4895cada5ba5a9f594ce9a5fdb0fa8@46.4.23.42:46656,224c85918ea98d62daab63ba9eceab195b676760@144.91.71.1:26656,ee41f0a7874d46cc71d2b47e40595e8a467e3141@89.163.142.13:26656,25d7a6c32516f18e3f45b0379460d8ed4e396b43@164.92.84.68:26656,f41685745f7cd74caa542829d291367ae1377ce0@34.74.30.133:26656,6f29a743ad237d435aac29b62528cea01ceb3ca9@46.4.91.90:26656,1c9706ea2df16ce46805b8653edf420724989483@185.106.94.95:26656,658168239d484fc5ad62563b5178cdfe7bba96af@173.249.18.11:39656,f8adb01e5932a42ff7d23d168853efa9352690e6@77.232.39.61:26656,a0ef091aed1da78640c84ea0ff81caaa55352bdc@43.159.194.246:26657,66dd5faabd4e09ba6bc0ab0093392064f454827c@185.215.167.74:26656,f2fa60742033345fb3f3aacb15d9815f5110485b@75.119.135.85:26656,eb3eb1afad693908e6da3d97c8d058e18f7f4304@38.242.159.204:26656,3c45677d6c6fed5e140bcbb78d60cfa79d155a79@148.251.82.143:26656,10e3f31fd0cfa829edfa6f855053d1e3cd93662e@5.75.249.183:26656,7b2e60ea260082f6cdd91ef6b3908d8f991beb7c@77.232.40.162:26656,49cf3a642a1a04044d3a4aaa555fa438babb698d@142.132.178.151:26656,4d523009433cbd75e9074af445c65c13454359a8@45.88.223.212:26656,63256b5937ac438e3b21b570a07ace6ddc3bd0c6@194.163.182.122:39656,4f1c8f3de055988bf15f21b666369287fb5230de@31.220.73.148:26656,816b6cfae5fbd04c5797b9b6703117ad9049b14a@65.21.91.50:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
