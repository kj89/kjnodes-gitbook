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
peers="6eb0d1b32e8166e2539f74c4f0810b3758891397@148.251.11.99:26656,77d89a919f28122c9ceef7be1d0dc761fd35a330@20.199.10.78:26656,46b2205032ff6f15ce8cdca7d225aca3d84db47d@45.85.146.7:39656,e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,6be3b4bb5e56724133a04ba979aa64cd7bc6b4fd@185.53.46.52:26656,8d29cdc290141bc1155d1b5d3eb6ee721b881ab7@95.216.163.211:26556,0bc611c38f435f2f2b8d2377a90147564d4a80fe@185.234.69.143:26656,a37f72e68e61b0dfbe01e7509753d27c5dc54ec9@157.245.148.64:39656,4d523009433cbd75e9074af445c65c13454359a8@45.88.223.212:26656,45c330a2c3b99a9c060f6911e33bb4f5eff3a286@83.171.248.30:26656,7b2e60ea260082f6cdd91ef6b3908d8f991beb7c@77.232.40.162:26656,2c43fe447b1d86f5a248b4fb042d960f5e71ed97@217.76.56.58:26656,5b2d7ccdf924ff16c3d0e3b55c4547a71c99dc42@161.97.122.167:39656,21c924f547ac7a4e1db6cb9f05cff3a972467c8f@65.109.49.226:39656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,0b370f7aaf505127be417635514d9ef31a43e9f7@178.128.53.194:26656,f25598fa32578246cafd25b9dad0841db5d5ef23@199.175.98.114:26656,64d2ea39df1cf635fccb17311c245b9fdc56194a@91.107.195.121:26656,4591a6d3bb34030aa3b7be72691e36eb72cd6eff@128.199.47.116:26656,9f06819b9ca5927310ffad266220ec2b1c2a0edc@82.165.207.203:39656,a0ef091aed1da78640c84ea0ff81caaa55352bdc@43.159.194.246:26657,736acf4bea85fc40b63093f018805e03c989bcce@75.119.143.229:26656,fa97f07b4d18db75fdf600dac0df8600040bf283@80.254.8.54:39656,35d8f676cf4db0f4ed7f3a8750daf8010797bdc4@135.181.116.109:26656,658168239d484fc5ad62563b5178cdfe7bba96af@173.249.18.11:39656,6fefa7ece2ff81d1c228c31eda72692d9299d8bc@38.242.248.145:26656,2434150d03943cf91d68eaf4dc8a3874b18139f6@5.199.136.56:39656,b8310e77f3e68c59010a3250034b7caf8139ac5d@135.181.205.249:26656,3c45677d6c6fed5e140bcbb78d60cfa79d155a79@148.251.82.143:26656,4d1780c1abcd7df29391bed1f5138af88424ce22@185.182.184.194:26656,c9e408e5a59ae4aed2a43f8c1f4b5cf505ae2917@35.228.47.215:26656,39dfeaa1cc3fda73074ec6cd92750a7076e5c2f9@194.163.181.0:26656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,6b9c920759355eb6614500c10e77eb138f28ed81@64.226.76.171:26656,743e880228429a217e5b6b87a76f677eb061db10@188.166.231.174:26656,92351b76e1ae57ae45e31a373447b60dada03d5b@75.119.153.120:26656,e0312a70844803297269124468f070a84f06777c@65.108.41.173:28056,4fb43c4d6bd6cf0f20781b67e437263a24e4153d@95.217.75.105:31656,f2fa60742033345fb3f3aacb15d9815f5110485b@75.119.135.85:26656,6f29a743ad237d435aac29b62528cea01ceb3ca9@46.4.91.90:26656,f2b77362c141f846c0bd8f795895bfe60589eaa7@185.237.96.110:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
