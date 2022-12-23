# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="d15e22d7be8ba1b97ff429cf87fea2af41450b37@149.102.134.212:41656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,e53572d91ae5c25caf23b6390467d1d2978ae3b7@65.109.14.17:26656,938ac1e4262cb2341bac323156fc3637f1b9c472@84.46.240.25:41656,4ef3c9bf8e304b6d7f557ecc0c255eeb16ba9518@65.108.235.107:41656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,794c20090098075af9b90e0914e548300b41a6a7@154.26.131.131:36656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,5fb72a0bea398ce56fa20cd732623f98d774be7d@149.102.128.208:41656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,ccf24b1e4f8566f3914c08e13d2b6154ed47ddbd@45.153.48.45:26656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,2ef464f5acb300ed319f18fb082c7455a05e7cca@89.163.209.88:26656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,12f6b84a23b054a6591c647c2a4456c40af65cce@5.9.147.22:24656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,b647cfd2cbeff0e4bceb476f8b0d78cfb6cda685@45.147.199.191:36656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,6eaed2ae1e4fdab63a492c55e7f465e0043b5b92@173.249.48.234:26656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,c3564f48561aea2fbace68395cb4661065bb54ac@164.92.185.204:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
